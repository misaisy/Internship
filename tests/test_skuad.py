import pytest
import httpx
import pytest_asyncio


BASE_URL = "http://www.skuad-dev.nots-fns.ru"

VALID_REGION = "Краснодарский край"
ALL_REGIONS = "all_regions"

@pytest_asyncio.fixture
async def async_client():
    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        yield client

class TestIndustry:
    ENDPOINT = "/api/squad-statement/region/indusdtry/"

    @pytest.mark.asyncio
    async def test_positive(self, async_client):
        """Позитивный тест с валидным регионом"""
        params = {"region_name": "Краснодарский край"}
        response = await async_client.get(self.ENDPOINT, params=params)
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0
        for item in data:
            assert "id" in item
            assert "name" in item
            assert "numComps" in item
            assert "profitComps" in item
            assert "unprofitComps" in item
            assert "taxespaidComps" in item
            assert "creddebtComps" in item
            assert "revenue" in item
            assert "taxesPaid" in item
            assert "creditDebt" in item

    @pytest.mark.asyncio
    async def test_negative(self, async_client):
        """Негативный тест без параметра region_name"""
        response = await async_client.get(self.ENDPOINT)
        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_boundary(self, async_client):
        """Граничный тест со значением all_regions"""
        params = {"region_name": ALL_REGIONS}
        response = await async_client.get(self.ENDPOINT, params=params)
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)


class TestBusinessActivity:
    ENDPOINT = "/api/squad-statement/region/business_activity/"

    @pytest.mark.asyncio
    async def test_positive(self, async_client):
        params = {"region_name": VALID_REGION}
        response = await async_client.get(self.ENDPOINT, params=params)
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, dict)
        assert "region_name" in data
        business_data = data["data_ba"]
        assert isinstance(business_data, list)
        assert len(business_data) > 0
    @pytest.mark.asyncio
    async def test_negative(self, async_client):
        response = await async_client.get(self.ENDPOINT)
        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_boundary(self, async_client):
        params = {"region_name": ALL_REGIONS}
        response = await async_client.get(self.ENDPOINT, params=params)
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, dict)
        assert "region_name" in data
        business_data = data["data_ba"]
        assert isinstance(business_data, list)
        assert len(business_data) > 0


class TestStatisticsRankSolvency:
    ENDPOINT = "/api/squad-statement/region/statistics-rank-solvency/"

    @pytest.mark.asyncio
    async def test_positive(self, async_client):
        params = {"region_name": VALID_REGION}
        response = await async_client.get(self.ENDPOINT, params=params)
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)

    @pytest.mark.asyncio
    async def test_negative(self, async_client):
        response = await async_client.get(self.ENDPOINT)
        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_boundary(self, async_client):
        params = {"region_name": ALL_REGIONS}
        response = await async_client.get(self.ENDPOINT, params=params)
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0

    @pytest.mark.asyncio
    async def test_boundary_limit(self, async_client):
        """Дополнительный граничный тест с несуществующим регионом"""
        params = {"region_name": VALID_REGION, "limit": 3}
        response = await async_client.get(self.ENDPOINT, params=params)
        assert response.status_code == 200