import React from 'react';
import { logoutUser } from '../api';

function Logout({ token, onLogout }) {
  const handleLogout = async () => {
    try {
      await logoutUser(token);
      onLogout();
    } catch (err) {
      console.error('Logout failed', err);
    }
  };

  return (
    <button onClick={handleLogout}>
      Logout
    </button>
  );
}

export default Logout;
