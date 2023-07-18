function Search({ handleChange, search }) {
  return (
    <div className="bg-amber-400 py-3 px-3 mt-2 rounded-sm">
      <form>
        <label className="mr-5" htmlFor="search">
          Search for your favorites!
        </label>
        <input
          className="rounded-md py-1 px-16 bg-amber-100 placeholder:text-stone-400"
          // style={{ width: "300px" }}
          type="text"
          id="search"
          name="search"
          value={search}
          placeholder="search here..."
          onChange={(e) => handleChange(e)}
        />
      </form>
    </div>
  );
}

export default Search;
