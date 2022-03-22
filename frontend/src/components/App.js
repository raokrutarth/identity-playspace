import logo from '../logo.svg';
import '../App.css';
import {
    BrowserRouter as Router,
    Routes,
    Route,
    Link
} from "react-router-dom";

import { FaCalendarAlt, FaDoorOpen, FaUsers } from "react-icons/fa";
import React, { Component } from 'react';

import ProposalsPage from "./Proposals/ProposalsPage";
import UnionsPage from "./Unions/UnionsPage";
import UnionsPicker from "./Unions/UnionsPicker";
import UsersPage from "./Users/UsersPage";

export default function App() {
    return (
        <Router>
            <div className="App">
                <header>
                    <nav>
                        <ul>
                            <li>
                                <Link to="/proposals" className="btn btn-header">
                                    <FaCalendarAlt />
                                    <span>Proposals</span>
                                </Link>
                            </li>
                            <li>
                                <Link to="/unions" className="btn btn-header">
                                    <FaDoorOpen />
                                    <span>Unions</span>
                                </Link>
                            </li>
                            <li>
                                <Link to="/users" className="btn btn-header">
                                    <FaUsers />
                                    <span>Members</span>
                                </Link>
                            </li>
                        </ul>
                    </nav>
                    <UnionsPicker />
                </header>
                <Routes>
                    <Route path="/proposals" element={<ProposalsPage />} />
                    <Route path="/unions" element={<UnionsPage />} />
                    <Route path="/users" element={<UsersPage />} />
                </Routes>
            </div>
        </Router>
    );
}
