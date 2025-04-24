import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './Component.css';

function UserVerification() {
  const [verifications, setVerifications] = useState([]);

  useEffect(() => {
    axios.get('/api/user-verification/verifications/')
      .then(response => setVerifications(response.data))
      .catch(error => console.error('Error fetching user verifications:', error));
  }, []);

  return (
    <div className="component">
      <h2>User Verifications</h2>
      {verifications.length === 0 ? (
        <p>No user verifications found.</p>
      ) : (
        <ul>
          {verifications.map(verification => (
            <li key={verification.user}>
              User: {verification.user} <br />
              Status: {verification.verification_status} <br />
              Method: {verification.verification_method} <br />
              Reputation Points: {verification.reputation_points}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default UserVerification;
