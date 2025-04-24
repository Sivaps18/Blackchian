import React, { useState, useEffect } from 'react';
import Login from './components/Login';
import Logout from './components/Logout';

function App() {
  const [token, setToken] = useState(() => localStorage.getItem('token'));

  useEffect(() => {
    if (token) {
      localStorage.setItem('token', token);
    } else {
      localStorage.removeItem('token');
    }
  }, [token]);

  const handleLogin = (newToken) => {
    setToken(newToken);
  };

  const handleLogout = () => {
    setToken(null);
  };

  return (
    <div className="App">
      {!token ? (
        <Login onLogin={handleLogin} />
      ) : (
        <div>
          <h1>Welcome!</h1>
          <Logout token={token} onLogout={handleLogout} />
          {/* Add other authenticated components here */}
        </div>
      )}
    </div>
  );
}

export default App;
