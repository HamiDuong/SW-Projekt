import React, { Component } from 'react';
import Select from '@mui/material/Select';
import MenuItem from '@mui/material/MenuItem';
import { Box } from '@mui/system';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';
import OverIndividualEntries from './OverIndividualEntries';
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
            return <OverIndividualEntries value={projectId} onChange={this.handleChange} />
        } else {
            return (
                <div>
                    <Alert sx={{ margin: 3 }} variant='outlined' severity="info">You haven´t selected a project yet.</Alert>
                </div>)
        }
    }

    render() {
        const projects = this.state.projects
        const func = this.showing()
        return (
            <Box>
                <h1>Nicht-Admin-Sicht</h1>
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

export default IndividualSelection;
