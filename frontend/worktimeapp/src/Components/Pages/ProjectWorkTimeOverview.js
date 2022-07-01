import React, { Component } from 'react';
import Select from '@mui/material/Select';
import MenuItem from '@mui/material/MenuItem';
import { Box } from '@mui/system';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';
import ActivityOverview from './ActivityOverview';
import Alert from '@mui/material/Alert';

class IndividualSelection extends Component {
    constructor(props) {
        super(props);
        this.state = {
            project: '',
            projects: [],
            temperature: '',
            projectName: '',
            selected: false,
            projectId: '',
            userId: this.props.userId,
        };
        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(e) {
        this.setState({
            projectId: e.target.value,
            selected: true,
        }, function () {
            console.log(this.state.projectId);
        })
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
        this.getProjectsForUser(this.state.userId)
    }


    showing() {
        const projectId = this.state.projectId
        if (this.state.selected) {
            return <ActivityOverview value={projectId} onChange={this.handleChange} />
        } else {
            return (
                <div>
                    <Alert sx={{ margin: 3 }} variant='outlined' severity="info">You haven´t selected a project yet.</Alert>
                </div>)
        }
    }

    render() {
        const projects = this.state.projects
        const showing = this.showing()
        return (
            <Box>
                <h2>Your booked projectworks</h2>
                <Select onChange={this.handleChange}>
                    {projects.map(project =>
                        project.map(elem => <MenuItem value={elem.id}>{elem.name}</MenuItem>)
                    )}
                </Select>
                <div>{showing}</div>
            </Box>
        );
    }
}

export default IndividualSelection;
