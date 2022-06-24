import React, { Component } from 'react';
import Select from '@mui/material/Select';
import MenuItem from '@mui/material/MenuItem';
import { Box } from '@mui/system';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';
import OverIndividualEntry from './OverIndividualEntries';


class MyWorkTimeOverview extends Component {
    constructor(props) {
        super(props);
        this.state = {
            project: this.props.id,
            projects: [],
            projectId: '',
            projectName: '',
            selected: false,
            user: '',
            userId: 1,
        };
        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(e) {
        this.setState({
            projectId: e.target.value,
            name: e.target.value,
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
        this.getProjectsForUser(this.state.userId)
    }


    showing() {
        if (this.state.selected) {
            return <div>
                <OverIndividualEntry onChange={this.handleChange} value={this.state.projectId} />
            </div>
        } else {
            return <h1>You haven´t selected a project yet.</h1>
        }
    }

    render() {
        const projects = this.state.projects
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

export default MyWorkTimeOverview;
