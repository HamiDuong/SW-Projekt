import React, { Component } from 'react';
import Select from '@mui/material/Select';
import MenuItem from '@mui/material/MenuItem';
import { Box } from '@mui/system';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';
import ActivityOverviewAdmin from './ActivityOverviewAdmin';
import Alert from '@mui/material/Alert';

class ProjectWorkTimeOverviewAdmin extends Component {
    /* 
    @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)
    In dieser Seite werden alle Aktivitäten, deren Informationen, sowie deren Buchungen und Bearbeitetenden User angezeigt. 
    */

    constructor(props) {
        super(props);
        this.state = {
            project: '',
            projects: [],
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
            selected: !this.state.selected,
        }, function () {
            console.log(this.state.projectId);
        })
    }


    getProjectsForAdmin = (id) => {
        WorkTimeAppAPI.getAPI().getAllProjectsForAdmin(id).then(projectBO =>
            this.setState({
                projects: [projectBO],
            }, function () {
                console.log(this.state.projects)
            }))
    }


    componentDidMount() {
        this.getProjectsForAdmin(this.state.userId)
    }

    componentDidUpdate(prevProps, prevState) {
        // only update if searchValue has changed
        if (prevState.selected !== this.state.selected) {
            this.getProjectsForAdmin(this.state.userId)
            this.setState({
                selected: true
            })
        }
    }


    render() {
        const projects = this.state.projects
        const projectId = this.state.projectId
        return (
            <div>
                <Box>
                    <h2>Overview of booked work for your projects</h2>
                    <Select onChange={this.handleChange}>
                        {projects.map(project =>
                            project.map(elem => <MenuItem value={elem.id}>{elem.name}</MenuItem>)
                        )}
                    </Select>
                    {this.state.selected ?
                        <ActivityOverviewAdmin value={projectId} onChange={this.handleChange} /> :
                        <Alert sx={{ margin: 3 }} variant='outlined' severity="info">You haven´t selected a project yet.</Alert>
                    }
                </Box>
            </div>

        );
    }
}

export default ProjectWorkTimeOverviewAdmin;
