import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './Component.css';

function Analytics() {
  const [metrics, setMetrics] = useState([]);

  useEffect(() => {
    axios.get('/api/analytics/analyticsmetric/')
      .then(response => setMetrics(response.data))
      .catch(error => console.error('Error fetching analytics metrics:', error));
  }, []);

  return (
    <div className="component">
      <h2>Analytics Metrics</h2>
      {metrics.length === 0 ? (
        <p>No analytics metrics found.</p>
      ) : (
        <ul>
          {metrics.map(metric => (
            <li key={metric.id}>
              Metric: {metric.metric_name} <br />
              Value: {metric.value} <br />
              Date: {new Date(metric.timestamp).toLocaleString()}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default Analytics;
