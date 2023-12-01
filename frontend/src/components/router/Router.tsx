import { Dialog } from '@headlessui/react';
import { lazy, Suspense, useState } from 'react';
import { Outlet, RouteObject, useRoutes, BrowserRouter } from 'react-router-dom';
import { LiaLightbulbSolid, LiaHomeSolid, LiaPlugSolid, LiaCloudUploadAltSolid, LiaPuzzlePieceSolid, LiaHistorySolid } from 'react-icons/lia';
import { IoShareSocialOutline, IoColorWand, IoMailOutline } from "react-icons/io5";
import { TbChartCandleFilled, TbPlusMinus, TbReportAnalytics, TbMessage } from "react-icons/tb";
import { GrLineChart, GrMoney } from "react-icons/gr";
import { BsPatchExclamationFill } from "react-icons/bs";
import { SlMagnifier } from "react-icons/sl";
import { PiListChecksBold, PiGraphBold } from "react-icons/pi";
import { LuLightbulb } from "react-icons/lu";

const Loading = () => <p className="p-4 w-full h-full text-center">Loading...</p>;

const IndexScreen = lazy(() => import('~/components/screens/Index'));
const Page404Screen = lazy(() => import('~/components/screens/404'));

function Layout() {
  return (
    <div className="drawer min-h-screen bg-base-200 lg:drawer-open">
      <input id="my-drawer" type="checkbox" className="drawer-toggle" />
      <Outlet />
      <aside className="drawer-side z-10">
        <label htmlFor="my-drawer" className="drawer-overlay"></label>
        <nav className="flex min-h-screen w-200 flex-col gap-2 overflow-y-auto bg-base-100 px-6 py-10">
          <div className="mx-4 flex items-center gap-2 font-black">
            <svg width="32" height="32" viewBox="0 0 1024 1024" fill="none" xmlns="http://www.w3.org/2000/svg">
              <rect x="256" y="670.72" width="512" height="256" rx="128" className="fill-base-content" />
              <circle cx="512" cy="353.28" r="256" className="fill-base-content" />
              <circle cx="512" cy="353.28" r="261" stroke="black" stroke-opacity="0.2" stroke-width="10" />
              <circle cx="512" cy="353.28" r="114.688" className="fill-base-100" />
            </svg>
            Daisy Corp
          </div>
          <ul className="menu">
            <li>
              <a className="active">
                <LiaHomeSolid /> Dashboard
              </a>
            </li>
            <li>
              <details>
                <summary>
                  <LiaPlugSolid /> Data Connection/Upload
                </summary>
                <ul>
                  <li>
                    <a><LiaPuzzlePieceSolid/> Integration Options</a>
                  </li>
                  <li>
                    <a><LiaCloudUploadAltSolid/> File Upload</a>
                  </li>
                  <li>
                    <a><IoShareSocialOutline/> Data Mapping Assistance</a>
                  </li>
                </ul>
              </details>
            </li>
            <li>
              <details>
                <summary>
                  <GrMoney/> Interactive P&L Statement
                </summary>
                <ul>
                  <li>
                    <a>
                      <BsPatchExclamationFill/> Anomalies detected <span className="badge badge-info badge-sm">12</span>
                    </a>
                  </li>
                  <li>
                    <a><SlMagnifier/> Drill-Down Capabilities</a>
                  </li>
                  <li>
                    <a><PiGraphBold/> Data Linkage Visualisation</a>
                  </li>
                  <li>
                    <a><LiaHistorySolid/> Historical Data Comparison</a>
                  </li>
                  <li>
                    <a><PiListChecksBold/> Go-Forward Tracking of Iniatitives</a>
                  </li>
                </ul>
              </details>
            </li>
            <li>
              <details>
                <summary>
                <TbPlusMinus/>
                  Value Levers
                </summary>
                <ul>
                  <li>
                    <a><TbChartCandleFilled/> List of Value Levers</a>
                  </li>
                  <li>
                    <a><IoColorWand/> Value Lever Wizard</a>
                  </li>
                  <li>
                    <a><GrLineChart/> KPI Tracking</a>
                  </li>
                  <li>
                    <a><LuLightbulb/> Recommendation Engine</a>
                  </li>
                  <li>
                    <a><TbReportAnalytics/> Impact Analysis</a>
                  </li>
                </ul>
              </details>
            </li>
            <li>
              <a>
                <IoMailOutline/> Messages<span className="badge badge-info badge-sm">12</span>
              </a>
            </li>
          </ul>
        </nav>
      </aside>
    </div>
  );
}

export const Router = () => {
  return (
    <BrowserRouter>
      <InnerRouter />
    </BrowserRouter>
  );
};

const InnerRouter = () => {
  const routes: RouteObject[] = [
    {
      path: '/',
      element: <Layout />,
      children: [
        {
          index: true,
          element: <IndexScreen />,
        },
        {
          path: '*',
          element: <Page404Screen />,
        },
      ],
    },
  ];
  const element = useRoutes(routes);
  return (
    <div>
      <Suspense fallback={<Loading />}>{element}</Suspense>
    </div>
  );
};
