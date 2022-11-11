/**
 * The default view that an authenticated user first sees when they visit the
 *  app. It renders a list of teams that the user is a member of, and a list
 *  of the api keys that the user has access to.
 * @module @cyclonedx/ui/sbom/views/Dashboard/Dashboard
 */
import * as React from 'react'
import { useNavigate, useLoaderData } from 'react-router-dom'
import Box from '@mui/material/Box'
import Container from '@mui/material/Container'
import Grid from '@mui/material/Grid'
import { useData } from '@/hooks/useData'
import { Team, TeamApiResponse } from '@/types'
import DashboardTeamCard from './Team/components/DashboardTeamCard'
import DashboardTeamCreationCard from './Team/components/DashboardTeamCreateCard'

const DashboardContainer = (): JSX.Element => {
  const navigate = useNavigate()

  // hook to get the helper method to update teams in the app data context
  const { setTeams } = useData()

  // hook for getting the route loader data
  const teams = useLoaderData() as Team[]

  // update teams in the data context from the route loader data
  // TODO: find a better way to do this or remove it and only use loader data
  /* eslint-disable react-hooks/exhaustive-deps */
  // the dependency array for this useEffect does not need setTeams.
  React.useEffect(() => {
    setTeams(teams)
  }, [teams])
  /* eslint-enable react-hooks/exhaustive-deps */

  // Helper function that redirects the user to the new team creation view.
  const navigateToCreateTeam = React.useCallback(() => navigate('team/new'), [])

  return (
    <Box sx={{ display: 'flex' }} data-testid="Dashboard">
      <Box
        sx={{
          flexGrow: 1,
          height: 'auto',
          overflow: 'auto',
        }}
      >
        <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
          <Grid container spacing={6} className="match-height">
            <Grid item xs={12} md={4}>
              <DashboardTeamCreationCard onClick={navigateToCreateTeam} />
            </Grid>

            {teams &&
              teams.map((team: TeamApiResponse) => (
                <Grid item xs={12} md={4} key={team.id}>
                  <DashboardTeamCard teamId={team.id} />
                </Grid>
              ))}
          </Grid>
        </Container>
      </Box>
    </Box>
  )
}
export default DashboardContainer
