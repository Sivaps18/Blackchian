import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './Component.css';

function ContentModeration() {
  const [actions, setActions] = useState([]);

  useEffect(() => {
    axios.get('/api/content-moderation/contentmoderationaction/')
      .then(response => setActions(response.data))
      .catch(error => console.error('Error fetching content moderation actions:', error));
  }, []);

  return (
    <div className="component">
      <h2>Content Moderation Actions</h2>
      {actions.length === 0 ? (
        <p>No content moderation actions found.</p>
      ) : (
        <ul>
          {actions.map(action => (
            <li key={action.id}>
              Action: {action.action_type} <br />
              Content ID: {action.content_id} <br />
              Status: {action.status} <br />
              Date: {new Date(action.timestamp).toLocaleString()}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default ContentModeration;
