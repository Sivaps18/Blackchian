const API_BASE_URL = 'http://localhost:8000'; // Django backend URL

export async function fetchProposals() {
  const response = await fetch(`${API_BASE_URL}/api/governance/proposals/`);
  if (!response.ok) {
    throw new Error('Failed to fetch proposals');
  }
  return await response.json();
}

export async function createProposal(proposalData) {
  const response = await fetch(`${API_BASE_URL}/api/governance/proposals/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(proposalData),
  });
  if (!response.ok) {
    throw new Error('Failed to create proposal');
  }
  return await response.json();
}

// New login function
export async function loginUser(username, password) {
  const response = await fetch(`${API_BASE_URL}/api/user-verification/login/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ username, password }),
  });
  if (!response.ok) {
    throw new Error('Login failed');
  }
  return await response.json(); // returns { token, user_id }
}

// New logout function
export async function logoutUser(token) {
  const response = await fetch(`${API_BASE_URL}/api/user-verification/logout/`, {
    method: 'POST',
    headers: {
      'Authorization': `Token ${token}`,
    },
  });
  if (!response.ok) {
    throw new Error('Logout failed');
  }
  return true;
}
