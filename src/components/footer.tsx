import React from 'react';

const Footer: React.FC = () => {
  return (
    <footer className="footer">
      <div className="container">
        <p>&copy; {new Date().getFullYear()} SwitchViz. All rights reserved.</p>
      </div>
    </footer>
  );
};

export default Footer;
