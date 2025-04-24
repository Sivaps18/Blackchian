import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './Component.css';

function Governance() {
  const [proposals, setProposals] = useState([]);

  useEffect(() => {
    axios.get('/api/governance/proposals/')
      .then(response => setProposals(response.data))
      .catch(error => console.error('Error fetching proposals:', error));
  }, []);

  return (
    <div className="component">
      <h2>Governance Proposals</h2>
      {proposals.length === 0 ? (
        <p>No proposals found.</p>
      ) : (
        <ul>
          {proposals.map(proposal => (
            <li key={proposal.proposal_id}>
              <strong>{proposal.proposal_type}</strong>: {proposal.proposal_content} <br />
              Status: {proposal.proposal_status} <br />
              Submitted by: {proposal.submitter} <br />
              Date: {new Date(proposal.timestamp).toLocaleString()}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default Governance;
