import React, { Component } from 'react';
import Select from '@mui/material/Select';
import MenuItem from '@mui/material/MenuItem';
import { InputLabel } from '@mui/material';
import { Button } from '@mui/material';
import { Box } from '@mui/system';
import OverTimeIndi from './IndividualTimes';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';

class ProjectSelectionNotAdmin extends Component {
    constructor(props) {
        super(props);
        this.state = {
            project: this.props.id,
            projects: [],
            temperature: '',
            projectName: '',
            selected: false,
            projectId: '',
        };
        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(e) {
        this.setState({
            temperature: e.target.value,
            selected: true
        });
    }


    getProjectsForUser = (id) => {
        WorkTimeAppAPI.getAPI().getAllProjectsForUser(id).then(projectBO =>
            this.setState({
                projects: [projectBO],
            }, function () {
                console.log(this.state.projects)
            }))
    }


    componentDidMount() {
        this.getProjectsForUser(1)
    }


    showing() {
        const temperature = this.state.temperature
        if (this.state.selected) {
            return <OverTimeIndi onChange={this.handleChange} value={this.state.temperature}
                celsius={(temperature)} />
        } else {
            return <h1>You haven´t selected a project yet.</h1>
        }
    }

    render() {
        const projects = this.state.projects
        const temperature = this.state.temperature
        const func = this.showing()
        return (
            <Box>
                <Select onChange={this.handleChange}>
                    {projects.map(project =>
                        project.map(elem => <MenuItem value={elem.id}>{elem.name}</MenuItem>)
                    )}
                </Select>
                <div>{func}</div>
            </Box>
        );
    }
}

export default ProjectSelectionNotAdmin;
