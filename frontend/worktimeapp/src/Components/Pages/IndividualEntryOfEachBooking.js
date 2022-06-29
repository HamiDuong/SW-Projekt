import React, { Component } from 'react';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';
import TableCell from '@mui/material/TableCell';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';


class IndividualEntriesOfEachBooking extends Component {
    constructor(props) {
        super(props);
        this.state = ({
            user_id: '',
            act_id: '',
            time: '',
            user: '',
            userName: '',
        })
    }

    getBookedTimeForUserOfAnActivity = (act_id, us_id) => {
        WorkTimeAppAPI.getAPI().getBookedTimeOfUserForAnActivity(act_id, us_id).then(time =>
            this.setState({
                time: time
            }, function () {
                console.log('Time:', this.state.time)
            }))
    }

    componentDidMount() {
        this.getBookedTimeForUserOfAnActivity(this.props.act_id, this.props.us_id)
        this.getUserById(this.props.us_id)
    }

    getUserById(id) {
        WorkTimeAppAPI.getAPI().getUserById(id).then(userBO =>
            this.setState({
                user: userBO,
                userName: userBO[0].first_name
            }, function () {
                console.log('Hier ist der User: ', this.state.user)
            }))
    }

    render() {
        return (<Paper>
            <Box
                sx={{
                    width: '100%',
                    display: 'inline-flex',
                    alignItems: 'center',
                    justifyContent: 'space-around',
                    border: (theme) => `1px solid ${theme.palette.divider}`,
                    bgcolor: 'background.paper',
                    color: 'text.secondary',
                    '& svg': {
                        m: 1.5,
                    },
                    '& hr': {
                        mx: 5,
                    },

                }}
            >

                <TableCell >{this.state.time}</TableCell>
                <TableCell >{this.props.capacity}</TableCell>
                <TableCell >{this.props.current_c}</TableCell>
            </Box>
        </Paper>
        );
    }
}

export default IndividualEntriesOfEachBooking;