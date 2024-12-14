from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task

class TaskModelTest(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="password123")
        # Create a sample task
        self.task = Task.objects.create(
            title="Test Task",
            description="This is a test task.",
            due_date="2024-12-31",
            priority="high",
            status="pending",
            assigned_user=self.user
        )

    def test_task_creation(self):
        """Test if a task is created successfully."""
        self.assertEqual(self.task.title, "Test Task")
        self.assertEqual(self.task.description, "This is a test task.")
        self.assertEqual(self.task.priority, "high")
        self.assertEqual(self.task.status, "pending")
        self.assertEqual(self.task.assigned_user, self.user)

    def test_task_str_representation(self):
        """Test the string representation of a task."""
        self.assertEqual(str(self.task), "Test Task")


class TaskAPITest(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="apiuser", password="password123")
        self.client.login(username="apiuser", password="password123")

    def test_create_task_api(self):
        """Test the task creation API endpoint."""
        response = self.client.post('/api/tasks/', {
            "title": "API Test Task",
            "description": "Testing task creation through API.",
            "due_date": "2024-12-31",
            "priority": "medium",
            "status": "pending",
            "assigned_user": self.user.id
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['title'], "API Test Task")

    def test_task_list_api(self):
        """Test the task list API endpoint."""
        Task.objects.create(
            title="Task 1",
            description="First task",
            due_date="2024-12-15",
            priority="low",
            status="pending",
            assigned_user=self.user
        )
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_task_detail_api(self):
        """Test retrieving task details through the API."""
        task = Task.objects.create(
            title="Task Detail Test",
            description="Detail retrieval test",
            due_date="2024-12-20",
            priority="high",
            status="pending",
            assigned_user=self.user
        )
        response = self.client.get(f'/api/tasks/{task.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], "Task Detail Test")
