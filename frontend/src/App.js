import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import Governance from './components/Governance';
import ContentModeration from './components/ContentModeration';
import UserVerification from './components/UserVerification';
import Analytics from './components/Analytics';
import RevenueSharing from './components/RevenueSharing';
import Compliance from './components/Compliance';
import './styles.css';

function App() {
  return (
    <div className="App">
      <nav>
        <ul className="nav-list">
          <li><Link to="/governance">Governance</Link></li>
          <li><Link to="/content-moderation">Content Moderation</Link></li>
          <li><Link to="/user-verification">User Verification</Link></li>
          <li><Link to="/analytics">Analytics</Link></li>
          <li><Link to="/revenue-sharing">Revenue Sharing</Link></li>
          <li><Link to="/compliance">Compliance</Link></li>
        </ul>
      </nav>
      <main>
        <Routes>
          <Route path="/governance" element={<Governance />} />
          <Route path="/content-moderation" element={<ContentModeration />} />
          <Route path="/user-verification" element={<UserVerification />} />
          <Route path="/analytics" element={<Analytics />} />
          <Route path="/revenue-sharing" element={<RevenueSharing />} />
          <Route path="/compliance" element={<Compliance />} />
        </Routes>
      </main>
    </div>
  );
}

export default App;
