import React from 'react';
function Logout() {
  const handleLogout = () => {
    alert('Logout flow would start here.');
  };
  return <button onClick={handleLogout}>Logout</button>;
}
export default Logout;
