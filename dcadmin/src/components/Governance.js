import React, { useEffect, useState } from 'react';
import { fetchProposals } from '../api';

function Governance() {
  const [proposals, setProposals] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchProposals()
      .then(data => setProposals(data))
      .catch(err => setError(err.message));
  }, []);

  return (
    <div>
      <h2>Governance Proposals</h2>
      {error && <p style={{color: 'red'}}>Error: {error}</p>}
      <ul>
        {proposals.map(proposal => (
          <li key={proposal.proposal_id}>
            {proposal.proposal_content} - Status: {proposal.proposal_status}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Governance;
