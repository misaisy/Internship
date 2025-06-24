import pytest
import httpx
import pytest_asyncio
from test_constants import *

@pytest_asyncio.fixture
async def async_client():
    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        yield client

class TestNegativeRegions:
    @pytest.mark.asyncio
    @pytest.mark.parametrize("endpoint", NEGATIVE_ENDPOINT)
    async def test_negative(self, async_client, endpoint):
        """Общий негативный тест для всех эндпоинтов."""
        response = await async_client.get(endpoint)
        assert response.status_code == 422


class TestIndustry:
    ENDPOINT = ENDPOINTS["INDUSTRY"]

    @pytest.mark.asyncio
    @pytest.mark.parametrize("region, fields", INDUSTDRY_VALID_REGIONS)
    async def test_positive(self, async_client, region, fields):
        """Позитивный тест."""
        params = {"region_name": region}
        response = await async_client.get(self.ENDPOINT, params=params)
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0
        for item in data:
            for field in fields:
                assert field in item

    @pytest.mark.asyncio
    @pytest.mark.parametrize("region, fields", INDUSDTRY_INVALID_REGIONS)
    async def test_negative_reg(self, async_client, region, fields):
        """Негативный тест."""
        params = {"region_name": region}
        response = await async_client.get(self.ENDPOINT, params=params)
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 0

    @pytest.mark.asyncio
    async def test_negative(self, async_client):
        """Негативный тест без параметра region_name."""
        response = await async_client.get(self.ENDPOINT)
        assert response.status_code == 422


class TestBusinessActivity:
    ENDPOINT = ENDPOINTS["BUSINESS_ACTIVITY"]

    @pytest.mark.asyncio
    @pytest.mark.parametrize("region, industry, fields", BUSINESS_VALID_REGIONS)
    async def test_positive(self, async_client, region, industry, fields):
        """Позитивный тест."""
        if industry != "":
            params = {"region_name": region, "industry_name": industry}
            response = await async_client.get(self.ENDPOINT, params=params)
            assert response.status_code == 200
            data = response.json()
            assert isinstance(data, dict)
            assert "region_name" in data
            business_data = data["data_ba"]
            assert isinstance(business_data, list)
            assert len(business_data) > 0
            for industry_item in business_data:
                assert "industry_name" in industry_item
                assert "business_activity" in industry_item
                business = industry_item["business_activity"]
                assert isinstance(business, list)
                assert len(business) > 0
                for item in business:
                    for field in fields:
                        assert field in item
        else:
            params = {"region_name": region}
            response = await async_client.get(self.ENDPOINT, params=params)
            assert response.status_code == 200
            data = response.json()
            assert isinstance(data, dict)
            assert "region_name" in data
            business_data = data["data_ba"]
            assert isinstance(business_data, list)
            assert len(business_data) > 0
            for industry_item in business_data:
                assert "industry_name" in industry_item
                assert "business_activity" in industry_item
                business = industry_item["business_activity"]
                assert isinstance(business, list)
                assert len(business) > 0
                for item in business:
                    for field in fields:
                        assert field in item


    @pytest.mark.asyncio
    @pytest.mark.parametrize("region, fields", BUSINESS_INVALID_REGIONS)
    async def test_negative_reg(self, async_client, region, fields):
        """Негативный тест."""
        params = {"region_name": region}
        response = await async_client.get(self.ENDPOINT, params=params)
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, dict)
        assert len(data) == 2
        assert len(fields) > 0
        for field in fields:
            assert field in data

    @pytest.mark.asyncio
    async def test_negative(self, async_client):
        """Негативный тест без параметра region_name."""
        response = await async_client.get(self.ENDPOINT)
        assert response.status_code == 422

    @pytest.mark.asyncio
    @pytest.mark.parametrize("region, fields", BUSINESS_BOUNDARY_REGIONS)
    async def test_boundary(self, async_client, region, fields):
        """Граничный тест."""
        params = {"region_name": region}
        response = await async_client.get(self.ENDPOINT, params=params)
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, dict)
        assert "region_name" in data
        business_data = data["data_ba"]
        assert isinstance(business_data, list)
        assert len(business_data) > 0
        for field in fields:
            assert field in data


class TestStatisticsRankSolvency:
    ENDPOINT = ENDPOINTS["STATISTICS"]

    @pytest.mark.asyncio
    @pytest.mark.parametrize("region, fields", STATISTIC_VALID_REGION)
    async def test_positive(self, async_client, region, fields):
        """Позитивный тест."""
        params = {"region_name": region}
        response = await async_client.get(self.ENDPOINT, params=params)
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        for item in data:
            for field in fields:
                assert field in item

    @pytest.mark.asyncio
    @pytest.mark.parametrize("region, fields", STATISTIC_INVALID_REGIONS)
    async def test_negative_reg(self, async_client, region, fields):
        """Негативный тест."""
        params = {"region_name": region}
        response = await async_client.get(self.ENDPOINT, params=params)
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 0
        for field in fields:
            assert field in data

    @pytest.mark.asyncio
    async def test_negative(self, async_client):
        """Негативный тест без параметра region_name."""
        response = await async_client.get(self.ENDPOINT)
        assert response.status_code == 422

    @pytest.mark.asyncio
    @pytest.mark.parametrize("region, fields", STATISTIC_ALL_REGION)
    async def test_boundary(self, async_client, region, fields):
        """Граничный тест."""
        params = {"region_name": "all_regions"}
        response = await async_client.get(self.ENDPOINT, params=params)
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0
        for item in data:
            for field in fields:
                assert field in item

    @pytest.mark.asyncio
    @pytest.mark.parametrize("limits", LIMITS)
    async def test_boundary_limit(self, async_client, limits):
        """Граничный тест с лимитом."""
        params = {"region_name": "all_regions", "limit": limits}
        response = await async_client.get(self.ENDPOINT, params=params)
        if limits == -1:
            assert response.status_code == 500
        else:
            assert response.status_code == 200
