import React, { useEffect, useState } from 'react';
import axiosInstance from '../api';
import './TaskList.css';

const TaskList = () => {
    const [tasks, setTasks] = useState([]);

    useEffect(() => {
        const fetchTasks = async () => {
            try {
                const response = await axiosInstance.get('/');
                setTasks(response.data);
            } catch (error) {
                console.error('Error fetching tasks:', error);
            }
        };

        fetchTasks();
    }, []);

    return (
        <div>
            <h1>Task List</h1>
            {tasks.map((task) => (
                <div key={task.id}>
                    <h2>{task.title}</h2>
                    <p>{task.description}</p>
                    <p>Due: {task.due_date}</p>
                    <p>Status: {task.status}</p>
                    <p>Priority: {task.priority}</p>
                </div>
            ))}
        </div>
    );
};

export default TaskList;
