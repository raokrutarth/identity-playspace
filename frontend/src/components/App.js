import logo from '../logo.svg';
import '../App.css';
import {
    BrowserRouter as Router,
    Routes,
    Route,
    Link
} from "react-router-dom";
import M from "materialize-css";
import { useEffect } from "react";

import { FaCalendarAlt, FaDoorOpen, FaUsers } from "react-icons/fa";

import ProposalsPage from "./Proposals/ProposalsPage";
import UnionsPage from "./Unions/UnionsPage";
import UnionsPicker from "./Unions/UnionsPicker";
import UsersPage from "./Users/UsersPage";

export default function App() {

    useEffect(() => {
        M.AutoInit();
    }, []);

    return (
        <Router>
            <div className="App">
                <header>
                    <nav>
                        <div className="nav-wrapper row">
                            <span className="right col s4"><UnionsPicker /></span>

                            <ul id="nav-mobile" className="left col hide-on-med-and-down">
                                <li>
                                    <Link to="/proposals">
                                        <FaCalendarAlt />
                                        <span>Proposals</span>
                                    </Link>
                                </li>
                                <li>
                                    <Link to="/unions">
                                        <FaDoorOpen />
                                        <span>Unions</span>
                                    </Link>
                                </li>
                                <li>
                                    <Link to="/users">
                                        <FaUsers />
                                        <span>Members</span>
                                    </Link>
                                </li>
                            </ul>
                        </div>

                    </nav>
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
