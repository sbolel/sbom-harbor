/**
 * Component that renders all routes in the application.
 * @module @cyclonedx/ui/sbom/Routes
 * @see {@link @cyclonedx/ui/sbom/Main} for usage.
 */
import * as React from 'react'
import { createHashRouter } from 'react-router-dom'

// ** Public Views
import SignIn from '@/views/SignIn/SignIn'
import SignOut from '@/views/SignOut/SignOut'

// ** Private Views
import App from '@/views/App/App'
import Dashboard from '@/views/Dashboard/Dashboard'
import TeamForm from '@/views/Dashboard/Team/TeamForm'
import TeamView from '@/views/Dashboard/Team/TeamView'

// ** Components
import Main from '@/Main'
import ErrorBoundary from '@/components/ErrorBoundary'
import NavigateToLogin from '@/components/react-router/NavigateToLogin'

// ** Loaders, Utils
import authLoader from '@/router/authLoader'
import teamLoader from '@/router/teamLoader'
import teamsLoader from '@/router/teamsLoader'
import configureCognito from '@/utils/configureCognito'

const router = createHashRouter([
  {
    path: '/',
    element: <Main />,
    loader: configureCognito,
    children: [
      {
        index: true,
        element: <NavigateToLogin />,
      },
      {
        path: 'login',
        element: <SignIn />,
      },
      {
        path: 'logout',
        element: <SignOut />,
      },
      {
        path: '*',
        element: <NavigateToLogin />,
      },
      {
        path: 'app/*',
        element: <App />,
        errorElement: <ErrorBoundary />,
        loader: authLoader,
        children: [
          {
            index: true,
            element: <Dashboard />,
            loader: teamsLoader,
            errorElement: <ErrorBoundary />,
          },
          {
            path: 'team',
            children: [
              {
                path: 'new',
                element: <TeamForm />,
              },
            ],
          },
          {
            path: 'teams/:teamId',
            loader: teamLoader,
            errorElement: <ErrorBoundary />,
            children: [
              {
                path: '',
                element: <TeamView />,
                loader: teamLoader,
                errorElement: <ErrorBoundary />,
              },
              {
                path: 'edit',
                element: <TeamForm />,
                loader: teamLoader,
                errorElement: <ErrorBoundary />,
              },
            ],
          },
        ],
      },
    ],
  },
])

export default router