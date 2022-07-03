import React, { Component } from 'react';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Collapse from '@mui/material/Collapse';
import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown';
import KeyboardArrowUpIcon from '@mui/icons-material/KeyboardArrowUp';
import IconButton from '@mui/material/IconButton';
import Box from '@mui/material/Box';
import ActivityBookingEntry from './ActivityEntryBookingsAdmin'
import ScheduleIcon from '@mui/icons-material/Schedule';
import Divider from '@mui/material/Divider';
import ListAltIcon from '@mui/icons-material/ListAlt';
import TaskAltIcon from '@mui/icons-material/TaskAlt';
import { TableContainer, TableCell } from '@mui/material';
import PersonIcon from '@mui/icons-material/Person';
import MoreTimeIcon from '@mui/icons-material/MoreTime';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';


class Entry extends Component {
    /* 
    @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)
    
    In dieser Komponente werden alle Aktivitäten und die zugehörigen Informationen aller ProjectUser abgespeichert. */
    constructor(props) {
        super(props);
        this.handleClick = this.handleClick.bind(this)
        this.state = ({
            activity: '',
            name: '',
            capacity: '',
            currentCapacity: '',
            activities: '',
            members: [],
            userIds: [],
            open: false,
            projectId: this.props.projectId,
            projectDuration: '',
            userCapacity: [],
            filterUsed: false,
            start: '',
            end: '',
        })
    }

    getActivity(id) {
        /** Holt Aktivität mithilfe deren Id und speichert die Informationen Aktivitätsname, geplante und gebuchte Kapazität*/
        WorkTimeAppAPI.getAPI().getActivityById(id).then(activityBO =>
            this.setState({
                activity: activityBO[0],
                name: activityBO[0].getName(),
                capacity: activityBO[0].capacity,
                currentCapacity: activityBO[0].currentCapacity
            }, function () {
                console.log(this.state.name, activityBO[0].capacity, 'HALLLLOOOO', this.state.currentCapacity)
            }))
    }

    getProjectUser(projectId) {
        /** Holt alle ProjectMembers mithilfe der ProjectId und speichert diese als Liste im State*/
        WorkTimeAppAPI.getAPI().getMembersByProjectId(projectId).then((member) => {
            /**Prüfung ob es Members zu diesem Projekt gibt*/
            if (member.length <= 0) {
                console.log('Weniger als 0')
                this.setState({
                    members: [0],
                    userIds: [0]
                })
            } else {
                this.setState({
                    members: member,
                }, function () {
                    console.log(this.state.members, 'Callback Function', typeof (this.state.members), this.state.userIds);
                    this.getUserIds();
                    this.getPlanedCapacitiesForUser();
                });

            }
        }
        )
    }

    getUserIds() {
        /** Holt die Ids der PRojectUser mithilfe der im State gespeichert ProjectMemberBOs 
        * und speichert diese als neue Liste im State ab.*/
        let members = this.state.members
        let liste = []
        let list_of_ids = []
        for (let i = 0; i < members.length; i++) {
            liste.push(this.state.members[i])
        }
        for (let i = 0; i < liste.length; i++) {
            list_of_ids.push(liste[i].getUserId())
        }
        this.setState({
            userIds: list_of_ids
        }, function () {
            console.log('2. Callbackfunction', this.state.userIds)
        })
    }

    getPlanedCapacitiesForUser() {
        /** Holt die geplante Kapazität der einzelnen ProjectMembers 
         * und speichert die Informationen in neuer Liste im State ab.*/
        let members = this.state.members
        let capacitiesOfUsers = []
        members.map(element =>
            capacitiesOfUsers.push(element.getCapacity()),
        )
        this.setState({
            userCapacity: [...this.state.userCapacity, ...capacitiesOfUsers]
        }, function () {
            console.log('Callbackfunction', this.state.userCapacity)
        })
    }

    getProjectDuration = (project_id) => {
        /** Holt Projectdauer mithilfe deren Id und speichert die Informationen als Liste im State ab.*/
        WorkTimeAppAPI.getAPI().getProjectDurationInDays(project_id).then(projectDurationBO =>
            this.setState({
                projectDuration: projectDurationBO
            }, function () {
                console.log('Hier ist der die Duration: ', this.state.projectDuration)

            }))
    }

    handleClick() {
        this.setState({
            open: !this.state.open,
        }, console.log('click'))
    }

    onFilterClicked = () => {
        this.setState({
            filterUsed: true
        })
    }

    removeFilterClicked = () => {
        this.setState({
            filterUsed: false
        })
    }

    componentDidMount() {
        this.getActivity(this.props.value)
        this.getProjectUser(this.props.projectId)
        this.getProjectDuration(this.props.projectId)
    }

    componentDidUpdate(prevProps, prevState) {
        if (prevState.filterUsed !== this.state.filterUsed) {
            let holder = document.getElementById('startFilter')
            let holder2 = document.getElementById('endFilter')
            this.setState({
                start: holder.value,
                end: holder2.value,
                userIds: [],
            })
            this.getActivity(this.props.value)
            this.getProjectUser(this.props.projectId)
            this.getProjectDuration(this.props.projectId)
        }
    }

    render() {
        const open = this.state.open
        return (
            <div>
                {this.state.filterUsed ?
                    <div>
                        <Box>
                            <Box
                                style={{
                                    display: 'flex',
                                    alignItems: 'center',
                                    justifyContent: 'center'
                                }}>
                                <TableContainer>
                                    <Table stickyHeader aria-label="sticky table">
                                        <TableBody>
                                            <Box
                                                style={{
                                                    display: 'flex',
                                                    alignItems: 'center',
                                                    justifyContent: 'left'
                                                }}>
                                                <IconButton aria-label="expand row"
                                                    size="small"
                                                    onClick={this.handleClick}>
                                                    {open ? <KeyboardArrowUpIcon /> : <KeyboardArrowDownIcon />}
                                                </IconButton>
                                                <TableRow>{this.state.name}</TableRow>
                                            </Box>
                                        </TableBody>
                                    </Table>
                                </TableContainer>
                            </Box>

                            <Collapse in={open} timeout="auto" unmountOnExit>
                                <TableContainer style={{
                                    display: 'flex',
                                    justifyContent: 'center'
                                }}>
                                    <Table sx={{ width: '75%' }}>
                                        <TableHead>
                                            <Box sx={{
                                                width: '50%',
                                                display: 'inline-flex',
                                                alignItems: 'center',
                                                justifyContent: 'left',
                                                border: (theme) => `1px solid ${theme.palette.divider}`,
                                                color: 'text.secondary',
                                                bgcolor: 'background.paper',
                                                '& svg': {
                                                    m: 2,
                                                },
                                                '& hr': {
                                                    mx: 1,
                                                },
                                            }}>
                                                <TableRow >Project duration (in days): {this.state.projectDuration} </TableRow>
                                                <Divider orientation="vertical" flexItem />
                                                <TableRow>Planed capacity : {this.state.capacity}</TableRow>
                                                <Divider orientation="vertical" flexItem />
                                                <TableRow>Total Booked Time: {this.state.currentCapacity} </TableRow>
                                            </Box>
                                        </TableHead>
                                    </Table>
                                </TableContainer>
                                <Box sx={{
                                    padding: 'auto',
                                    margin: 'auto',
                                    justifyContent: 'right',
                                    width: '75%',
                                    display: 'flex',
                                    alignItems: 'center'
                                }}>
                                    <TextField defaultValue={this.state.start} format={'YYYY/MM/DD'} type="date" id="startFilter" inputProps={
                                        { readOnly: true, }
                                    } />
                                    <TextField defaultValue={this.state.end} format={'YYYY/MM/DD'} type="date" id="endFilter" inputProps={
                                        { readOnly: true, }
                                    } />
                                    <Button onClick={this.removeFilterClicked}>Remove Filter</Button>

                                </Box>
                                <TableContainer style={{
                                    display: 'flex',
                                    justifyContent: 'center',
                                }}>
                                    <Table sx={{ width: '75%' }}>
                                        <TableHead>
                                            <Box sx={{
                                                width: '100%',
                                                display: 'inline-flex',
                                                alignItems: 'center',
                                                justifyContent: 'space-evenly',
                                                border: (theme) => `1px solid ${theme.palette.divider}`,
                                                bgcolor: 'background.paper',
                                                color: 'text.secondary',
                                                '& svg': {
                                                    m: 2,
                                                },
                                                '& hr': {
                                                    mx: 1,
                                                },

                                            }}>
                                                <TableRow><ListAltIcon />Booked capacity</TableRow>
                                                <Divider orientation="vertical" />
                                                <TableRow><PersonIcon />Employees</TableRow>
                                                <Divider orientation="vertical" />
                                                <TableRow > <TaskAltIcon />Planed capacity of employee</TableRow>

                                            </Box>
                                        </TableHead>
                                        <TableBody>
                                            {this.state.userIds.map((element, index) => {
                                                console.log(element, 'Ist das hier eine UserId?')
                                                return (
                                                    <ActivityBookingEntry start={this.state.start} end={this.state.end} filterTrigger={this.state.filterUsed} act_id={this.props.value} us_id={element} capacity={this.state.capacity} current_c={this.state.currentCapacity} projectId={this.state.projectId}
                                                        user_capa={this.state.userCapacity[index]} />)
                                            })}
                                        </TableBody>
                                    </Table>
                                </TableContainer>
                            </Collapse>
                        </Box>
                    </div > :
                    <div>
                        <Box
                            style={{
                                display: 'flex',
                                alignItems: 'center',
                                justifyContent: 'center'
                            }}>
                            <TableContainer>
                                <Table stickyHeader aria-label="sticky table">
                                    <TableBody>
                                        <Box
                                            style={{
                                                display: 'flex',
                                                alignItems: 'center',
                                                justifyContent: 'left'
                                            }}>
                                            <IconButton aria-label="expand row"
                                                size="small"
                                                onClick={this.handleClick}>
                                                {open ? <KeyboardArrowUpIcon /> : <KeyboardArrowDownIcon />}
                                            </IconButton>
                                            <TableRow>{this.state.name}</TableRow>
                                        </Box>
                                    </TableBody>
                                </Table>
                            </TableContainer>
                        </Box>

                        <Collapse in={open} timeout="auto" unmountOnExit>
                            <TableContainer style={{
                                display: 'flex',
                                justifyContent: 'center'
                            }}>
                                <Table sx={{ width: '75%' }}>
                                    <TableHead>
                                        <Box sx={{
                                            width: '50%',
                                            display: 'inline-flex',
                                            alignItems: 'center',
                                            justifyContent: 'left',
                                            border: (theme) => `1px solid ${theme.palette.divider}`,
                                            color: 'text.secondary',
                                            bgcolor: 'background.paper',
                                            '& svg': {
                                                m: 2,
                                            },
                                            '& hr': {
                                                mx: 1,
                                            },
                                        }}>
                                            <TableRow >Project duration (in days): {this.state.projectDuration} </TableRow>
                                            <Divider orientation="vertical" flexItem />
                                            <TableRow>Planed capacity : {this.state.capacity}</TableRow>
                                            <Divider orientation="vertical" flexItem />
                                            <TableRow>Total Booked Time: {this.state.currentCapacity} </TableRow>
                                        </Box>
                                    </TableHead>
                                </Table>
                            </TableContainer>
                            <Box sx={{
                                padding: 'auto',
                                margin: 'auto',
                                justifyContent: 'right',
                                width: '75%',
                                display: 'flex',
                                alignItems: 'center'
                            }} >
                                <TextField format={'YYYY/MM/DD'} type="date" id="startFilter" />
                                <TextField format={'YYYY/MM/DD'} type="date" id="endFilter" />
                                <Button onClick={this.onFilterClicked} >Filtering</Button>
                            </Box>
                            <TableContainer style={{
                                display: 'flex',
                                justifyContent: 'center',
                            }}>
                                <Table sx={{ width: '75%' }}>
                                    <TableHead>
                                        <Box sx={{
                                            width: '100%',
                                            display: 'inline-flex',
                                            alignItems: 'center',
                                            justifyContent: 'space-evenly',
                                            border: (theme) => `1px solid ${theme.palette.divider}`,
                                            bgcolor: 'background.paper',
                                            color: 'text.secondary',
                                            '& svg': {
                                                m: 2,
                                            },
                                            '& hr': {
                                                mx: 1,
                                            },

                                        }}>
                                            <TableRow><ListAltIcon />Booked capacity</TableRow>
                                            <Divider orientation="vertical" />
                                            <TableRow><PersonIcon />Employees</TableRow>
                                            <Divider orientation="vertical" />
                                            <TableRow > <TaskAltIcon />Planed capacity of employee</TableRow>

                                        </Box>
                                    </TableHead>
                                    <TableBody>
                                        {this.state.userIds.map((element, index) => {
                                            console.log(element, 'UserId')
                                            return (
                                                <ActivityBookingEntry start={this.state.start} end={this.state.end} filterTrigger={this.state.filterUsed} act_id={this.props.value} us_id={element} capacity={this.state.capacity} current_c={this.state.currentCapacity} projectId={this.state.projectId}
                                                    user_capa={this.state.userCapacity[index]} />)
                                        })}
                                    </TableBody>
                                </Table>
                            </TableContainer>
                        </Collapse>
                    </div >
                }

            </div >
        );
    }
}

export default Entry;
