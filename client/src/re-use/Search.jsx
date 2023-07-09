function Search({ onSearch, search }) {
  return (
    <div>
      <form>
        <label htmlFor="search">Search for your favorites!</label>
        <input
          type="text"
          id="search"
          name="search"
          value={search}
          onChange={(e) => onSearch(e)}
        />
      </form>
    </div>
  );
}

export default Search;
