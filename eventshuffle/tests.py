from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from eventshuffle.models import Event, EventDate
from datetime import datetime


class EventTests(APITestCase):
    def test_create_event(self):
        url = reverse('event-create')
        testName = 'Best event'
        firstDate = '2024-10-01'
        secondDate = '2024-10-02'
        data = {
            'name': testName,
            'dates': [firstDate, secondDate]
        }
        response = self.client.post(url, data, format='json')

        # Test that output is correct
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.json())
        self.assertIsInstance(response.json()['id'], int)
        self.assertGreater(response.json()['id'], 0)

        # Test that database is correct
        newEvent = Event.objects.get(name=testName)
        self.assertEqual(newEvent.name, testName)

        newDates = EventDate.objects.filter(event=newEvent)
        self.assertEqual(len(newDates), 2)
        self.assertEqual(newDates[0].date, datetime.strptime(firstDate, '%Y-%m-%d').date())
        self.assertEqual(newDates[1].date, datetime.strptime(secondDate, '%Y-%m-%d').date())


    def test_event_list(self):
        url = reverse('event-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('events', response.json())



    def test_get_specific_event(self):
        testName = 'Test Event'
        testDate = '2024-10-01'
        event = Event.objects.create(name=testName)
        EventDate.objects.create(event=event, date=testDate, people=[])
        url = reverse('event-show', args=[event.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('id', response.json())
        self.assertIn('name', response.json())
        self.assertIn('dates', response.json())

    def test_add_vote(self):
        testName = 'Test Event'
        testDate = '2024-12-24'
        testPerson = 'John Doe'
        event = Event.objects.create(name=testName)
        EventDate.objects.create(event=event, date=testDate, people=[])
        url = reverse('add-vote', args=[event.id])
        data = {
            'name': testPerson,
            'votes': [testDate]
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('id', response.json())
        self.assertIn('name', response.json())
        self.assertIn('dates', response.json())
        self.assertEqual(len(response.json()['dates']), 1)
        self.assertIn('votes', response.json())
        self.assertEqual(len(response.json()['votes']), 1)

        # Test that database is correct
        newEvent = Event.objects.get(name=testName)

        newDates = EventDate.objects.filter(event=newEvent)
        self.assertEqual(len(newDates), 1)
        self.assertEqual(newDates[0].date, datetime.strptime(testDate, '%Y-%m-%d').date())
        self.assertEqual(newDates[0].people, [testPerson])


    def test_get_results(self):
        testName = 'Test Event'
        testDate = '2024-12-24'
        testPerson = 'John Doe'
        event = Event.objects.create(name=testName)
        EventDate.objects.create(event=event, date=testDate, people=[testPerson])
        url = reverse('get-results', args=[event.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('id', response.json())
        self.assertIn('suitableDates', response.json())
