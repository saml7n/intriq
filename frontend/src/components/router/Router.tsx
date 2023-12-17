import { Dialog } from '@headlessui/react';
import { ReactNode, lazy, useState } from 'react';
import {
  Outlet,
  RouteObject,
  useRoutes,
  BrowserRouter,
  useNavigate,
  createBrowserRouter,
  RouterProvider,
  redirect,
} from 'react-router-dom';
import {
  LiaLightbulbSolid,
  LiaHomeSolid,
  LiaPlugSolid,
  LiaCloudUploadAltSolid,
  LiaPuzzlePieceSolid,
  LiaHistorySolid,
} from 'react-icons/lia';
import { IoShareSocialOutline, IoColorWand, IoMailOutline } from 'react-icons/io5';
import { TbChartCandleFilled, TbPlusMinus, TbReportAnalytics, TbMessage } from 'react-icons/tb';
import { GrLineChart, GrMoney } from 'react-icons/gr';
import { BsPatchExclamationFill } from 'react-icons/bs';
import { SlMagnifier } from 'react-icons/sl';
import { PiListChecksBold, PiGraphBold } from 'react-icons/pi';
import { LuLightbulb } from 'react-icons/lu';
import { NavigationProvider, useNavigation } from '~/lib/NavigationContext';
import Loadable from '../shared/Loadable';
import { DefaultService as api, ApiError, OpenAPI } from '~/lib/client';
import Start from '~/components/screens/Start';
import CompanySetup from '../screens/CompanySetup';
import Page404 from '../screens/404';
import DataConnectAdd from '../screens/DataConnectAdd';
import DataConnect from '../screens/DataConnect';
import InsightDiscovery from '../screens/InsightDiscovery';
import InitiativeTracking from '../screens/InitiativeTracking';
import DashboardExample from '../screens/DashboardExample';

interface NavigationLinkProps {
  children: ReactNode;
  stepIndex: number;
  url: string;
}

OpenAPI.BASE = import.meta.env.VITE_API;

const NavigationStep: React.FC<NavigationLinkProps> = ({ url, stepIndex, children }) => {
  const { activeStep, setActiveStep, completedStep, setCompletedStep } = useNavigation();
  const navigate = useNavigate();

  const isActiveStep = activeStep === stepIndex;
  const isNextStep = stepIndex === completedStep + 1;
  const isCompleted = stepIndex <= completedStep;

  return (
    <li className={`step ${isNextStep ? 'step-primary' : isCompleted ? 'step-success' : ''}`}>
      <button
        className={`btn btn-block justify-start ${isCompleted ? '' : isNextStep ? 'btn-primary' : 'btn-disabled'} ${
          isActiveStep && !isNextStep ? 'btn-outline' : isNextStep ? '' : 'btn-ghost'
        }`}
        onClick={() => navigate(url)}
      >
        {children}
      </button>
    </li>
  );
};

function Layout() {
  return (
    <div className="drawer min-h-screen bg-base-200 lg:drawer-open">
      <input id="my-drawer" type="checkbox" className="drawer-toggle" />
      <main className="drawer-content">
        <Outlet />
      </main>
      <aside className="drawer-side z-40" style={{ scrollBehavior: 'smooth', scrollPaddingTop: '5rem' }}>
        <label htmlFor="my-drawer" className="drawer-overlay"></label>
        <nav className="flex min-h-screen w-200 flex-col gap-2 overflow-y-auto bg-base-100 px-6 py-10">
          <div className="mx-4 flex items-center gap-2 font-black">INTRIQ</div>
          <ul className="steps steps-vertical">
            <NavigationStep url="/setup-company" stepIndex={1}>
              <LiaHomeSolid /> Setup Company
            </NavigationStep>
            <NavigationStep url="/connect-data" stepIndex={2}>
              <LiaPlugSolid /> Connect Data
            </NavigationStep>
            <NavigationStep url="/discover-insights" stepIndex={3}>
              <PiGraphBold /> Discover Insights
            </NavigationStep>
            <NavigationStep url="/track-initiatives" stepIndex={4}>
              <GrLineChart /> Track Initiatives
            </NavigationStep>
            <NavigationStep url="/dashboard-example" stepIndex={5}>
              <GrLineChart /> Dashboard
            </NavigationStep>
          </ul>
        </nav>
      </aside>
    </div>
  );
}

const routes: RouteObject[] = [
  {
    path: '/',
    element: <Layout />,
    errorElement: <Page404 />,
    children: [
      {
        index: true,
        element: <Start />,
      },
      {
        path: 'setup-company/:companyId',
        loader: async ({ request, params }) => {
          return api.readCompanyCompanyIdGet(parseInt(params.companyId!)).catch((error) => {
            if ((error.status = 404)) {
              return redirect("/setup-company");
            } else throw error;
          });
        },
        element: <CompanySetup />,
      },
      {
        path: 'setup-company',
        element: <CompanySetup />,
      },
      {
        path: 'connect-data/add',
        element: <DataConnectAdd />,
      },
      {
        path: 'connect-data',
        element: <DataConnect />,
        loader: async ({ request, params }) => {
          return api.readDocumentsDocumentsGet().catch((error) => {
            if ((error.status = 404)) {
              return [];
            } else throw error;
          });
        },
      },
      {
        path: 'discover-insights',
        element: <InsightDiscovery />,
      },
      {
        path: 'track-initiatives',
        element: <InitiativeTracking />,
      },
      {
        path: 'dashboard-example',
        element: <DashboardExample />,
      },
      {
        path: '*',
        element: <Page404 />,
      },
    ],
  },
];

let router = createBrowserRouter(routes);

if (import.meta.hot) {
  import.meta.hot.dispose(() => router.dispose());
}

export const Router = () => {
  return (
    <NavigationProvider>
      <RouterProvider router={router} />
    </NavigationProvider>
  );
};
