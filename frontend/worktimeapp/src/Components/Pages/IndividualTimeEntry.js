import { TextField } from '@mui/material';
import React from 'react';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';

class IndividualTimeEntry extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            project: '',
            project_name: '',
        }

    }

    getAProjectByName = (name) => {
        WorkTimeAppAPI.getAPI().getProjectByName(name).then(projectBOs =>
            this.setState({
                project: projectBOs,
                project_name: projectBOs[0].name
            }, function () {
                console.log(projectBOs[0].name)
            }))
    }

    componentDidMount() {
        this.getAProjectByName('Neues Projekt')
    }


    render() {
        return (
            <div>
                <h1>{this.state.project_name}</h1>
            </div>
        );
    }
}

export default IndividualTimeEntry;