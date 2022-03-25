import M from "materialize-css";
import { useEffect } from "react";

export default function UsersPage() {
    useEffect(() => {
        M.AutoInit();
    }, []);

    return (
        <div className="users-page container">
            <div>
                <ul className="collection">

                    <li className="collection-item avatar">
                        <i className="material-icons circle">account_circle</i>
                        <span className="title">Title</span>
                        <p>First Line <br />
                            Second Line
                        </p>
                        <a href="#!" className="secondary-content"><i className="material-icons">grade</i></a>
                    </li>
                    <li className="collection-item avatar">
                        <i className="material-icons circle green">insert_chart</i>
                        <span className="title">Title</span>
                        <p>First Line <br />
                            Second Line
                        </p>
                        <a href="#!" className="secondary-content"><i className="material-icons">grade</i></a>
                    </li>
                    <li className="collection-item avatar">
                        <i className="material-icons circle red">account_circle</i>
                        <span className="title">Title</span>
                        <p>First Line <br />
                            Second Line
                        </p>
                        <a href="#!" className="secondary-content"><i className="material-icons">grade</i></a>
                    </li>
                </ul>
            </div>

            <div className="divider"></div>

            <div className="collection">
                <a href="#!" className="collection-item"><span className="badge">1</span>Alan</a>
                <a href="#!" className="collection-item"><span className="new badge">4</span>Alan</a>
                <a href="#!" className="collection-item">Alan</a>
                <a href="#!" className="collection-item"><span className="badge">14</span>Alan</a>
            </div>
        </div>
    );
}