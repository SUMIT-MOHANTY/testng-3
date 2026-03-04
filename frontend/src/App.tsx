import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import Dashboard from './routes/Dashboard';
import Login from './components/Login';
import Logout from './components/Logout';
import ProtectedRoute from './components/ProtectedRoute';

function App() {
  return (
    <div>
      <nav>
        <Link to="/">Home</Link> | <Link to="/dashboard">Dashboard</Link> | <Link to="/login">Login</Link> | <Link to="/logout">Logout</Link>
      </nav>
      <Routes>
        <Route path="/" element={<h2>Welcome</h2>} />
        <Route path="/login" element={<Login />} />
        <Route path="/logout" element={<Logout />} />
        <Route path="/dashboard" element={<ProtectedRoute><Dashboard /></ProtectedRoute>} />
      </Routes>
    </div>
  );
}
export default App;
