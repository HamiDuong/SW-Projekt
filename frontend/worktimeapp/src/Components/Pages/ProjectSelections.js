import React, { Component } from 'react';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI'

class ProjectSelection extends Component {
    constructor(props) {
        super(props);
        this.state = {
            projects: [],
        }
    }

    getAllProjects = () => {
        WorkTimeAppAPI.getAPI().getAllProjects().then(projectBOs =>
            this.setState({
                projects: projectBOs
            }, function () {
                console.log(this.state.projects)
            }))
    }

    componentDidMount() {
        this.getAllProjects()
    }

    render() {
        return (
            <div>
                {this.state.projects.map(elem => <div>{elem.name}</div>)}
            </div>
        );
    }
}

export default ProjectSelection;

//Wie weit bin ich gekommen:
//Die Namen werden mir korrekt angezeigt aber als Überschriften.
//Ich will diese Komponente verwenden um alle Projektnamen für die Übersicht in den TimeOverviews einzufügen (statt Projekt A, etc.)