'use client';
import React, { useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import {
    faXmark,
    faPlus,
    faCaretDown,
} from '@fortawesome/free-solid-svg-icons';

interface DropdownProps {
    id: string;
    label: string;
    options: string[];
    placeholder: string;
}

const Dropdown: React.FC<DropdownProps> = ({
    id,
    label,
    options,
    placeholder,
}) => {
    const [selectedItems, setSelectedItems] = useState<string[]>([]);

    const handleSelectionChange = (option: string) => {
        setSelectedItems((prevSelectedItems) =>
            prevSelectedItems.includes(option)
                ? prevSelectedItems.filter((item) => item !== option)
                : [...prevSelectedItems, option]
        );
    };

    const clearSelections = () => {
        setSelectedItems([]);
    };

    return (
        <div className="border-solid border-2 border-sky-500 p-2 relative">
            <label
                htmlFor={id}
                className="absolute top-0 scale-75 -translate-y-1 text-red-500"
            >
                {label}
            </label>
            <div className="border-solid border-2 border-slate-500 border-r-2">
                <div>{/* Selected items */}</div>
                <input
                    id={id}
                    type="text"
                    className="m-2"
                    placeholder={placeholder}
                />
                <div>
                    <FontAwesomeIcon
                        icon={faXmark}
                        onClick={() => clearSelections()}
                    />
                    <FontAwesomeIcon icon={faCaretDown} />
                </div>
                <ul>
                    {options.map((option) => (
                        <li
                            key={option}
                            className="cursor-pointer"
                            onClick={() => handleSelectionChange(option)}
                        >
                            {selectedItems.includes(option) ? (
                                <FontAwesomeIcon icon={faXmark} />
                            ) : (
                                <FontAwesomeIcon icon={faPlus} />
                            )}
                            <label className="cursor-pointer">{option}</label>
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
};

export default Dropdown;
