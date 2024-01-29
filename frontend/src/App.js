import React, { useState, useEffect } from 'react';
import axios from 'axios';

const App = () => {
    const [tasks, setTasks] = useState([]);
    const [newTask, setNewTask] = useState('');

    useEffect(() => {
        axios.get('http://sila-backend:5000/tasks')
            .then(response => setTasks(response.data))
            .catch(error => console.error('Error fetching tasks:', error));
    }, []);

    const addTask = () => {
        axios.post('http://sila-backend:5000/tasks', { title: newTask })
            .then(() => {
                setNewTask('');
                updateTasks();
            })
            .catch(error => console.error('Error adding task:', error));
    };

    const updateTasks = () => {
        axios.get('http://sila-backend:5000/tasks')
            .then(response => setTasks(response.data))
            .catch(error => console.error('Error fetching tasks:', error));
    };

    const deleteTask = (taskId) => {
        axios.delete(`http://sila-backend:5000/tasks/${taskId}`)
            .then(() => updateTasks())
            .catch(error => console.error('Error deleting task:', error));
    };

    return (
        <div>
            <h1>Todo List</h1>
            <ul>
                {tasks.map(task => (
                    <li key={task.id}>
                        {task.title}
                        <button onClick={() => deleteTask(task.id)}>Delete</button>
                    </li>
                ))}
            </ul>
            <div>
                <input
                    type="text"
                    value={newTask}
                    onChange={(e) => setNewTask(e.target.value)}
                />
                <button onClick={addTask}>Add Task</button>
            </div>
        </div>
    );
};

export default App;
