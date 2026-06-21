import "../../style/elements/bentoCard.css"
import "../../style/main/section.css";
import { BasicTable } from "./table";

const Attendance = () => {
    return (
        <main>
            <section className="section">
                <h1>hello</h1>
                <BasicTable />
            </section>
            <section className="section">
                <div className="container">
                    <div className="section__header">
                        <p className="section__eyebrow">// Weather Chatbot</p>
                        <h1 className="section__title">OverView About <br />My Project</h1>
                    </div>

                    <div className="bento__grid">
                        <div className="bento-card bento-card--wide reveal">
                            <p className="bento-card__number">no.01</p>
                            <h1 className="bento-card__title">SmartFarm AI Advisor</h1>
                            <h6 className="bento-card__text">
                                An AI-powered farming assistant that helps farmers make weather-related decisions using climate data, air-quality data, machine learning predictions, and an AI agent.
                            </h6>
                        </div>

                        <div className="bento-card bento-card--narrow bento-card--safety">
                            <p className="bento-card__number">no.02</p>
                            <h1 className="bento-card__title">Users</h1>
                            <h6>
                                <ul className="bento-card__text">
                                    <li>Farmers</li>
                                    <li>Agricultural cooperatives</li>
                                    <li>Small farms</li>
                                    <li>Agricultural students</li>
                                </ul>
                            </h6>
                        </div>

                        <div className="bento-card bento-card--mid bento-card--dark">
                            <p className="bento-card__number">no.03</p>
                            <h1 className="bento-card__title">Core Features</h1>
                            <h6>
                                <p className="bento-card__text">
                                    Will it rain tomorrow?
                                    <br />Should I water my tomatoes today?
                                    <br />Is air quality safe for my greenhouse?
                                    <br />How will climate change affect this area?
                                </p>
                            </h6>
                        </div>
                        <div className="bento-card bento-card--mid">
                            <p className="bento-card__number">no.04</p>
                            <h1 className="bento-card__title">Climate Change Insights</h1>
                            <h6>
                                <p className="bento-card__text">
                                    Temperature trends
                                    <br />Future warming projections
                                    <br />Climate risk indicators
                                </p>
                            </h6>
                        </div>
                    </div>
                </div>
            </section>
        </main>
    )
}

export { Attendance }