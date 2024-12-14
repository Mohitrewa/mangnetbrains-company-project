import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axiosInstance from '../api';

const TaskDetails = () => {
    const { id } = useParams();
    const [task, setTask] = useState(null);

    useEffect(() => {
        const fetchTask = async () => {
            try {
                const response = await axiosInstance.get(`/${id}/`);
                setTask(response.data);
            } catch (error) {
                console.error('Error fetching task details:', error);
            }
        };

        fetchTask();
    }, [id]);

    return (
        <div>
            {task ? (
                <>
                    <h1>{task.title}</h1>
                    <p>{task.description}</p>
                    <p>Due: {task.due_date}</p>
                    <p>Status: {task.status}</p>
                    <p>Priority: {task.priority}</p>
                </>
            ) : (
                <p>Loading...</p>
            )}
        </div>
    );
};

export default TaskDetails;
