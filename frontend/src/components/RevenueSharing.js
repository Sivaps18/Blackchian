import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './Component.css';

function RevenueSharing() {
  const [shares, setShares] = useState([]);

  useEffect(() => {
    axios.get('/api/revenue-sharing/shares/')
      .then(response => setShares(response.data))
      .catch(error => console.error('Error fetching revenue shares:', error));
  }, []);

  return (
    <div className="component">
      <h2>Revenue Sharing</h2>
      {shares.length === 0 ? (
        <p>No revenue shares found.</p>
      ) : (
        <ul>
          {shares.map(share => (
            <li key={share.share_id}>
              User: {share.user} <br />
              Amount: {share.amount} <br />
              Source: {share.source} <br />
              Date: {new Date(share.timestamp).toLocaleString()}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default RevenueSharing;
