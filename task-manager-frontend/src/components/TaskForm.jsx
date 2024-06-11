// create a form for adding/editing tasks
import React, {useState} from 'react';
const TaskForm = ({ onSubmit, initialData = {} }) => {
    const [title, setTitle] = useState(initialData.title || '');
    const [description, setDescription] = useState(initialData.description || '');
    const [dueDate, setDueDate] = useState(initialData.dueDate || '');
    const [priority, setPriority] = useState(initialData.priority || 'Medium');
    const [status, setStatus] = useState(initialData.status || 'Pending');
  
    const handleSubmit = (e) => {
      e.preventDefault();
      onSubmit({ title, description, dueDate, priority, status });
    };
  
    return (
      <form onSubmit={handleSubmit}>
        <div>
          <label>Title:</label>
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Description:</label>
          <textarea
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Due Date:</label>
          <input
            type="date"
            value={dueDate}
            onChange={(e) => setDueDate(e.target.value)}
          />
        </div>
        <div>
          <label>Priority:</label>
          <select value={priority} onChange={(e) => setPriority(e.target.value)}>
            <option value="Low">Low</option>
            <option value="Medium">Medium</option>
            <option value="High">High</option>
          </select>
        </div>
        <div>
          <label>Status:</label>
          <select value={status} onChange={(e) => setStatus(e.target.value)}>
            <option value="Pending">Pending</option>
            <option value="In Progress">In Progress</option>
            <option value="Completed">Completed</option>
          </select>
        </div>
        <button type="submit">Save Task</button>
      </form>
    );
  };
  
  export default TaskForm;