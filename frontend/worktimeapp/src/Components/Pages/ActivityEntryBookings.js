import React, { Component } from 'react';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';
import TableCell from '@mui/material/TableCell';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';

class ActivityEntryBookings extends Component {
    /* 
    @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)
    
    In dieser Komponente werden alle Aktivitäten und deren Buchungen eines User abgespeichert. */
    constructor(props) {
        super(props);
        this.state = ({
            user_id: '',
            act_id: '',
            time: '',
            filteredTime: '',
            user: '',
            projectDuration: '',
            show_info: false,
            start: '',
            end: '',
        })
    }

    getBookedTimeByActivityIdAndProjectId = (act_id, us_id) => {
        /** Lädt die tatsächlich geleistete Projektarbeit eines Users mithilfe dessen Id und der Aktivity Id 
         *  und speichert die gebuchte Zeit im State ab.*/
        WorkTimeAppAPI.getAPI().getBookedTimeOfUserForAnActivity(act_id, us_id).then(time =>
            this.setState({
                time: time
            }, function () {
                console.log('Time:', this.state.time)
            }))
    }

    getBookedTimeByActivityIdAndProjectIdAndTimeFrame = (act_id, us_id, start, end) => {
        /** Lädt die tatsächlich geleistete Projektarbeit eines jeden Project-Users mithilfe dessen Id und der Aktivity Id 
         *  und speichert die gebuchten Zeiten im State ab.*/
        WorkTimeAppAPI.getAPI().getBookedTimesOfUserForAnActivityWithTimeframe(act_id, us_id, start, end).then(time =>
            this.setState({
                filteredTime: time
            }, function () {
                console.log('FilteredTime:', this.state.filteredTime)
            }))
    }

    componentDidMount = () => {
        if (this.props.filterTrigger == false) {
            this.getBookedTimeByActivityIdAndProjectId(this.props.act_id, this.props.us_id);
        } else {
            this.getBookedTimeByActivityIdAndProjectIdAndTimeFrame(this.props.act_id, this.props.us_id, this.props.start, this.props.end);
        }
    }

    render() {
        return (
            <div>
                {this.props.filterTrigger ?
                    <Box>
                        <Paper
                            sx={{ width: '100%', margin: 'auto' }}
                            style={{ display: 'inline-flex', justifyContent: 'space-around' }}
                        >
                            <TableCell>{this.state.filteredTime}</TableCell>
                            <TableCell>{this.props.user_capa}</TableCell>
                        </Paper>
                    </Box> :
                    <Box>
                        <Paper
                            sx={{ width: '100%', margin: 'auto' }}
                            style={{ display: 'inline-flex', justifyContent: 'space-around' }}
                        >
                            <TableCell>{this.state.time}</TableCell>
                            <TableCell>{this.props.user_capa}</TableCell>
                        </Paper>
                    </Box>
                }

            </div>
        );
    }
}

export default ActivityEntryBookings;