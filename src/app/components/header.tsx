import React from 'react';

const Header: React.FC = () => {
  return (
    <header className="header">
      <div className="container">
        <a href="#"><h1 className="logo">SwitchViz</h1></a>
        <nav className="nav">
          <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#data-source">Data Source</a></li>
            <li><a href="#about">About</a></li>

          </ul>
        </nav>
      </div>
    </header>
  );
};

export default Header;