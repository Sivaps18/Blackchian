import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Governance from './components/Governance';
import Analytics from './components/Analytics';
import Compliance from './components/Compliance';
import ContentModeration from './components/ContentModeration';
import RevenueSharing from './components/RevenueSharing';
import UserVerification from './components/UserVerification';

function AppRoutes() {
  return (
    <Router>
      <nav>
        <ul>
          <li><Link to="/governance">Governance</Link></li>
          <li><Link to="/analytics">Analytics</Link></li>
          <li><Link to="/compliance">Compliance</Link></li>
          <li><Link to="/content-moderation">Content Moderation</Link></li>
          <li><Link to="/revenue-sharing">Revenue Sharing</Link></li>
          <li><Link to="/user-verification">User Verification</Link></li>
        </ul>
      </nav>
      <Routes>
        <Route path="/governance" element={<Governance />} />
        <Route path="/analytics" element={<Analytics />} />
        <Route path="/compliance" element={<Compliance />} />
        <Route path="/content-moderation" element={<ContentModeration />} />
        <Route path="/revenue-sharing" element={<RevenueSharing />} />
        <Route path="/user-verification" element={<UserVerification />} />
        <Route path="*" element={<Governance />} />
      </Routes>
    </Router>
  );
}

export default AppRoutes;
