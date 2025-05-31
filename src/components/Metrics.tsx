import React from 'react';
import Dropdown from './Dropdown';

const Metrics: React.FC = () => {
    return (
        <div className="my-10">
            <h2>Metrics</h2>
            <p>Metrics content goes here.</p>
            <div>
                <Dropdown
                    id="cats"
                    label="Keyboard Switch Names"
                    options={['Option 1', 'Option 2', 'Option 3']}
                />
            </div>
        </div>
    );
};

export default Metrics;
