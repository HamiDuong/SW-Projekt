import React, { Component } from 'react';
import { Button, Table, TableBody, TableCell, TableHead, TableRow } from '@mui/material';
import { Box } from '@mui/system';
import { TableContainer } from '@mui/material';
import Paper from '@mui/material/Paper';
import TablePagination from '@mui/material/TablePagination';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';

class OverTimeEntry extends Component {
    constructor(props) {
        super(props);
        this.state = {
            projectId: this.props.value,
            activities: [],
            capacity: [],
            current_capacity: '',
            employees: '',
            activity_names: [],
            activity: false,

        }
    }

    componentDidMount() {
        this.getActivitiesForProject(this.props.value)
        console.log('Hier sind die props: ', this.props.value)
    }

    getActivitiesForProject = (project) => {
        WorkTimeAppAPI.getAPI().getActivitiesByProjectId(project).then(element =>
            this.setState({
                activities: [...this.state.activities, element],
            }, console.log('hier ist getActivties, dass in ProjectName aufgerufen wird'),
                this.checkActivities(element)
            ))
    }

    checkActivities = (element) => {
        try {
            this.getCapacities(element);
            this.getCurrentCapacities(element);
            this.getActivityNames(element)

        } catch (e) {
            console.log(e);
        }
    }



    getActivities = () => {
        WorkTimeAppAPI.getAPI().getAllActivities().then(activity =>
            this.setState({
                activities: [...this.state.activities, activity],
            }, this.getCapacities(activity),
                this.getCurrentCapacities(activity),
                this.getActivityNames(activity)
            ))
    }


    getCapacities = (arr) => {
        const acti = this.state.activities
        let i = 0
        while (i <= acti.length) {
            this.setState({
                capacity: [...this.state.capacity, arr[i].capacity]
            }, function () {
                console.log(this.state.capacity)
            })
            i = i + 1
        }
    }

    getCurrentCapacities = (arr) => {
        const acti = this.state.activities
        let i = 0
        while (i <= acti.length) {
            this.setState({
                current_capacity: [...this.state.current_capacity, arr[i].current_capacity]
            }, function () {
                console.log('CC', this.state.current_capacity)
            })
            i = i + 1
        }
    }

    getActivityNames = (arr) => {
        const acti = this.state.activities
        let i = 0
        while (i <= acti.length) {
            this.setState({
                activity_names: [...this.state.activity_names, arr[i].name]
            }, function () {
                console.log('AN', this.state.activity_names)
            })
            i = i + 1
        }
    }

    columns() {
        const columns = [
            {
                id: 'activity',
                label: 'Activities',
                minWidth: 170
            },
            {
                id: 'capacity',
                label: 'Capacity in (h)',
                minWidth: 100
            },
            {
                id: 'current_capacity',
                label: 'Booked Time in (h)',
                minWidth: 170,
                align: 'right',
                format: (value) => value.toLocaleString('de-DE'),
            },
            {
                id: 'employee',
                label: 'Employee',
                minWidth: 170,
                align: 'right',
                format: (value) => value.toLocaleString('en-US'),
            },
            {
                id: 'delta',
                label: 'Delta (h)',
                minWidth: 170,
                align: 'right',
                format: (value) => value.toFixed(2),
            },
        ];
        return columns
    }

    createData(activity, capacity, current_capacity) {
        const delta = capacity - current_capacity;
        return { activity, capacity, current_capacity, delta };
    }

    smth() {
        let newthingy = []
        const activities = this.state.activity_names
        const planedTimes = this.state.capacity
        const bookedTimes = this.state.current_capacity
        const employees = []

        for (var i = 0; i <= activities.length; i++) {
            let new_data = this.createData(activities[i], planedTimes[i], bookedTimes[i])
            newthingy.push(new_data)
        }
        return newthingy
    }


    render() {
        const rows = this.smth()
        const columns = this.columns()
        return (
            <diV>
                <Box sx={{ margin: 3 }} style={{
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                }}>
                    <Paper sx={{ width: '80%' }}>
                        <TableContainer sx={{ maxHeight: 440 }}>
                            <Table stickyHeader aria-label="sticky table">
                                <TableHead>
                                    <TableRow>
                                        <TableCell align="left" colSpan={0}>
                                            {this.state.project}
                                        </TableCell>
                                        <TableCell align="left" colSpan={6}>
                                            Details
                                        </TableCell>
                                    </TableRow>
                                    <TableRow>
                                        {columns.map((column) => (
                                            <TableCell
                                                key={column.id}
                                                align={column.align}
                                                style={{ minWidth: column.minWidth }}
                                            >
                                                {column.label}
                                            </TableCell>
                                        ))}

                                    </TableRow>
                                </TableHead>
                                <TableBody>
                                    {rows.map((row) => {
                                        return (
                                            <TableRow hover  >
                                                {columns.map((column) => {
                                                    const value = row[column.id];
                                                    return (
                                                        <TableCell align={column.align}>
                                                            {value}
                                                        </TableCell>
                                                    );
                                                })}
                                            </TableRow>
                                        );
                                    })}
                                </TableBody>
                            </Table>
                        </TableContainer>
                    </Paper>
                </Box>
            </diV>
        );
    }

}

export default OverTimeEntry;