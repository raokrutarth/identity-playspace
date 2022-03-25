import { useState, Fragment, useEffect } from "react";
import staticData from "../../static.json";

function ProposalsList() {
    const union = 3;
    const proposalsInUnion = staticData.proposals.filter(b => b.union === union);
    const [proposalIndex, setProposalIndex] = useState(0);
    const proposal = proposalsInUnion[proposalIndex];

    useEffect(() => {
        document.title = "Proposals picker page";

        return () => {
            console.log("unmounting proposal picker")
            document.title = "done"
        }
    }, []);

    return (

        <Fragment>
            <div>
                <ul className="porposals items-list-nav">
                    {proposalsInUnion.map((b, i) => (
                        <li
                            key={b.id}
                            className={i === proposalIndex ? "selected" : null}
                        >
                            <button
                                className="btn"
                                onClick={() => setProposalIndex(i)}
                            >
                                {b.name}
                            </button>
                        </li>
                    ))}
                </ul>
            </div>

            <div className="proposal-details">
                <div className="item">
                    <div className="item-header">
                        <h2>
                            {proposal.name}
                        </h2>
                    </div>
                    <p>{proposal.notes}</p>

                    <div className="item-details">
                        <h3>Meeting Times</h3>
                        <div className="proposal-deadline">
                            <ul>
                                {proposal.days
                                    .sort()
                                    .map(d => <li key={d}>{staticData.days[d]}</li>)
                                }
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </Fragment>

    );
}

export default ProposalsList;