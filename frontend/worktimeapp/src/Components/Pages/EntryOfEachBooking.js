import React, { Component } from 'react';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';
import TableCell from '@mui/material/TableCell';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Alert from '@mui/material/Alert';


class ActivityBookingEntry extends Component {
    constructor(props) {
        super(props);
        this.state = ({
            user_id: '',
            act_id: '',
            time: '',
            user: '',
            userName: '',
            projectDuration: '',
            show_info: false,
        })
    }

    getBookedTimeByActivityIdAndProjectId = (act_id, us_id) => {
        WorkTimeAppAPI.getAPI().getBookedTimeOfUserForAnActivity(act_id, us_id).then(time =>
            this.setState({
                time: time
            }, function () {
                console.log('Time:', this.state.time)
            }))
    }

    componentDidMount = () => {
        this.getProjectDuration(this.props.projectId)
        if (this.props.us_id == 0) {
            this.setState({
                userName: '-',
                time: '-',
                show_info: true
            })
        }
        else {
            this.getBookedTimeByActivityIdAndProjectId(this.props.act_id, this.props.us_id)
            console.log('Was passiert hier?', this.props.us_id)
            this.getUserById(this.props.us_id)

        }
    }

    getUserById(id) {
        WorkTimeAppAPI.getAPI().getUserById(id).then(userBO =>
            this.setState({
                user: userBO[0],
                userName: userBO[0].getFirstName()
            }, function () {
                console.log('Hier ist der User: ', this.state.user)
            }))
    }


    getProjectDuration = (project_id) => {
        WorkTimeAppAPI.getAPI().getProjectDurationInDays(project_id).then(projectDurationBO =>
            this.setState({
                projectDuration: projectDurationBO
            }, function () {
                console.log('Hier ist der die Duration: ', this.state.projectDuration)
            }))
    }

    render() {
        return (
            <Box>
                {this.state.show_info ?
                    <div>
                        <Paper sx={{ width: '100%' }}>
                            <TableCell width={150}></TableCell>
                            <TableCell width={300}>{this.state.time}</TableCell>
                            <TableCell width={350}>{this.state.userName}</TableCell>
                            <TableCell width={350}>{this.props.current_c}</TableCell>
                            <TableCell width={350}>{this.props.capacity}</TableCell>
                            <TableCell width={200}>{this.state.projectDuration}</TableCell>
                        </Paper>
                        <Alert sx={{ margin: 3 }} variant='outlined' severity="info">There are no project members for your project yet.</Alert></div> :
                    <Paper sx={{ width: '100%' }}>
                        <TableCell width={150}></TableCell>
                        <TableCell width={300}>{this.state.time}</TableCell>
                        <TableCell width={350}>{this.state.userName}</TableCell>
                        <TableCell width={350}>{this.props.current_c}</TableCell>
                        <TableCell width={350}>{this.props.capacity}</TableCell>
                        <TableCell width={200}>{this.state.projectDuration}</TableCell>
                    </Paper>
                }

            </Box>


        );
    }
}

export default ActivityBookingEntry;