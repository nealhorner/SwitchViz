import React from 'react';

const Footer: React.FC = () => {
    return (
        <footer className="footer">
            <div className="py-4 flex flex-col items-start justify-center gap-8 md:flex-row md:items-center md:justify-center">
                <p>
                    &copy; {new Date().getFullYear()} SwitchViz. All rights
                    reserved.
                </p>
                <p>
                    <a href="https://github.com/ThereminGoat">ThereminGoat</a>
                </p>
                <p>
                    <a href="https://github.com/nealhorner/SwitchViz">GitHub</a>
                </p>
            </div>
        </footer>
    );
};

export default Footer;
