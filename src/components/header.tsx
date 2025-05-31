import React from 'react';
import Image from 'next/image';
import Link from 'next/link';

const Header: React.FC = () => {
    return (
        <header>
            <div className="flex justify-between">
                <Link
                    href="#"
                    className="p-3 text-xl flex content-center gap-1 leading-9"
                >
                    <Image
                        src="/logo.png"
                        alt="SwitchViz logo"
                        width={36}
                        height={36}
                        priority
                    />
                    <h1 className="font-bold hover:underline">SwitchViz</h1>
                </Link>
                <nav className="p-3">
                    <ul className="flex justify-end gap-5 leading-9">
                        <li className="hover:underline">
                            <Link href="#home">Metrics</Link>
                        </li>
                        <li className="hover:underline">
                            <Link href="#data-source">Data Source</Link>
                        </li>
                        <li className="hover:underline">
                            <Link href="#about">About</Link>
                        </li>
                    </ul>
                </nav>
            </div>
        </header>
    );
};

export default Header;
