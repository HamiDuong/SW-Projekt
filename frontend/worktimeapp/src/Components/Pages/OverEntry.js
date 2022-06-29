import React, { Component } from 'react';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';
import Entry from './Entry';
import Alert from '@mui/material/Alert';
import Stack from '@mui/material/Stack';


class OverEntry extends Component {
    constructor(props) {
        super(props);
        this.state = ({
            projectId: this.props.value,
            activities: [],
            capacity: [],
            current_capacity: [],
            activity_names: [],
            userId: this.props.userId,
            activities_vorhanden: false,
        })
    }

    getActivitiesForProject = (project) => {
        WorkTimeAppAPI.getAPI().getActivitiesByProjectId(project).then(activity =>
            this.setState({
                activities: [...this.state.activities, activity],
            }, this.checkActivities(activity)
            ))
    }


    getCapacityofUserForProject = (act_id, us_id) => {
        WorkTimeAppAPI.getAPI().getBookedTimeOfUserForAnActivity(act_id, us_id).then(activity =>
            this.setState({
                current_capacity: [...this.state.current_capacity, activity],
            }, function () {
                console.log(this.state.current_capacity)
            }
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

    checkActivities = (element) => {
        try {
            this.getCapacityofUserForProject(element[0].id, this.state.userId);
            this.getCapacities(element);
            this.getActivityNames(element);
            this.setState({ activities_vorhanden: true })

        } catch (e) {
            console.log(e);

        }
    }

    componentDidMount() {
        this.getActivitiesForProject(this.props.value)
        console.log('this.props.value')

    }


    funcy() {
        let len = this.state.activities.length
        let liste = this.state.activities[0]
        console.log(liste, len, 'hier ist wahrscheinlich was falsch...')
        if (this.state.activities_vorhanden == true) {
            return (
                <div>
                    {liste.map((element, index) => {
                        console.log('Was ist hier?', element, index)
                        const value = element.id
                        console.log(value, 'VALUE', this.state.projectId)
                        return (
                            <Entry projectId={this.state.projectId} value={value} />
                        )
                    })}
                </div>
            )
        } else {
            return (
                <div> Keine Aktivitäten vorhanden</div>
            )
        }

    }


    render() {
        return (
            <div>
                {
                    this.state.activities_vorhanden ?
                        this.funcy()
                        : <div>
                            <Alert sx={{ margin: 3 }} variant='outlined' severity="info">There are no activities for your project yet.</Alert>
                        </div>
                }
            </div>
        );
    }
}

export default OverEntry;