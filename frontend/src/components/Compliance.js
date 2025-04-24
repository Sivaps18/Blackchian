import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './Component.css';

function Compliance() {
  const [records, setRecords] = useState([]);

  useEffect(() => {
    axios.get('/api/compliance/compliancerecord/')
      .then(response => setRecords(response.data))
      .catch(error => console.error('Error fetching compliance records:', error));
  }, []);

  return (
    <div className="component">
      <h2>Compliance Records</h2>
      {records.length === 0 ? (
        <p>No compliance records found.</p>
      ) : (
        <ul>
          {records.map(record => (
            <li key={record.id}>
              Record ID: {record.id} <br />
              Description: {record.description} <br />
              Status: {record.status} <br />
              Date: {new Date(record.timestamp).toLocaleString()}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default Compliance;
