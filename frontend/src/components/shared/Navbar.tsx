function Navbar() {
    return (
<div className="bg-base-100 text-base-content sticky top-0 z-30 flex h-16 w-full justify-center bg-opacity-90 backdrop-blur transition-shadow duration-100 [transform:translate3d(0,0,0)] shadow-sm">
        <nav className="navbar w-full sticky bg-base-100 top-0 z-30 flex items-center plr-2 gap-2 lg:gap-4">
          <span className="tooltip tooltip-bottom before:text-xs before:content-[attr(data-tip)]">
            <label aria-label="Open menu" htmlFor="my-drawer" className="btn btn-square btn-ghost drawer-button lg:hidden ">
              <svg
                width="20"
                height="20"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                className="inline-block h-5 w-5 stroke-current md:h-6 md:w-6"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M4 6h16M4 12h16M4 18h16"
                ></path>
              </svg>
            </label>
          </span>
          <div className="grow">
            <h1 className="lg:text-2xl lg:font-light">Setup Company</h1>
          </div>
          <div>
            <input type="text" placeholder="Search" className="input input-sm rounded-full max-sm:w-24" />
          </div>
          <div className="dropdown-end dropdown z-10">
            <div tabIndex={0} className="avatar btn btn-circle btn-ghost">
              <div className="w-10 rounded-full">
                <img src="https://picsum.photos/80/80?5" />
              </div>
            </div>
            <ul tabIndex={0} className="menu dropdown-content mt-3 w-52 rounded-box bg-base-100 p-2 shadow-2xl">
              <li>
                <a>Settings</a>
              </li>
              <li>
                <a>Logout</a>
              </li>
            </ul>
          </div>
        </nav>
      </div>
    );
}

export default Navbar;