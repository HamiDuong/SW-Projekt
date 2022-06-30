
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
        console.log('Was passiert hier?', this.props.us_id, this.props.act_id)
        this.getBookedTimeByActivityIdAndProjectId(this.props.act_id, this.props.us_id)
        this.getUserById(this.props.us_id)

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


    render() {
        return (
            <Box>

                <Paper sx={{ width: '100%', margin: 'auto' }}>
                    <TableCell width={250}></TableCell>
                    <TableCell width={400}>{this.state.time}</TableCell>
                    <TableCell width={500}>{this.state.userName}</TableCell>
                    <TableCell width={350}>{this.props.user_capa}</TableCell>

                </Paper>


            </Box>


        );
    }
}

export default ActivityBookingEntry;