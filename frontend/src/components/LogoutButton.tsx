import React from 'react';
import { useAuth } from '../context/AuthContext';
const LogoutButton: React.FC = () => {
  const { logout } = useAuth();
  const handle = async () => { await logout(); };
  return <button onClick={handle}>Logout</button>;
};
export default LogoutButton;
